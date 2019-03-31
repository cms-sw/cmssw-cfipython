import FWCore.ParameterSet.Config as cms

ctppsOpticalFunctionsESSource = cms.ESSource('CTPPSOpticalFunctionsESSource',
  validityRange = cms.EventRange('0:18446744073709551615-0:18446744073709551615'),
  opticalFunctions = cms.VPSet(
  ),
  scoringPlanes = cms.VPSet(
  ),
  appendToDataLabel = cms.string('')
)
