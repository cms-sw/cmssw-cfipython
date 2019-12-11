import FWCore.ParameterSet.Config as cms

ctppsLHCInfoRandomXangleESSource = cms.ESSource('CTPPSLHCInfoRandomXangleESSource',
  label = cms.string(''),
  generateEveryNEvents = cms.uint32(1),
  xangleHistogramFile = cms.string(''),
  xangleHistogramObject = cms.string(''),
  beamEnergy = cms.double(0),
  betaStar = cms.double(0),
  appendToDataLabel = cms.string('')
)
