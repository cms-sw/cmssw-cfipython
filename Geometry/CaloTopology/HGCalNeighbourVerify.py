import FWCore.ParameterSet.Config as cms

def HGCalNeighbourVerify(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalNeighbourVerify',
    nameDetector = cms.string('HGCalHESiliconSensitive'),
    waferU = cms.int32(2),
    waferV = cms.int32(0),
    cellU = cms.int32(10),
    cellV = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
