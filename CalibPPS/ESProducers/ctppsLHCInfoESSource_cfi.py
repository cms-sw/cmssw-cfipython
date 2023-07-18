import FWCore.ParameterSet.Config as cms

ctppsLHCInfoESSource = cms.ESSource('CTPPSLHCInfoESSource',
  label = cms.string(''),
  validityRange = cms.EventRange('0:18446744073709551615-0:18446744073709551615'),
  beamEnergy = cms.double(0),
  betaStar = cms.double(0),
  xangle = cms.double(0),
  appendToDataLabel = cms.string('')
)
