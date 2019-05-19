import FWCore.ParameterSet.Config as cms

hcalGeomCheck = cms.EDAnalyzer('HcalGeomCheck',
  caloHitSource = cms.string('HcalHits'),
  ietaMin = cms.untracked.int32(-41),
  ietaMax = cms.untracked.int32(41),
  depthMax = cms.untracked.int32(7),
  rMin = cms.untracked.double(0),
  rMax = cms.untracked.double(5500),
  zMin = cms.untracked.double(-12500),
  zMax = cms.untracked.double(12500),
  nBinR = cms.untracked.int32(550),
  nBinZ = cms.untracked.int32(250),
  verbosity = cms.untracked.int32(0)
)
