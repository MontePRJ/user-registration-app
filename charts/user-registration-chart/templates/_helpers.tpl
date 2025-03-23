{{/*
Return the fully qualified app name.
*/}}
{{- define "user-registration-chart.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Return the chart name.
*/}}
{{- define "user-registration-chart.name" -}}
{{- .Chart.Name -}}
{{- end }}

{{/*
Return the chart version.
*/}}
{{- define "user-registration-chart.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version -}}
{{- end }}
