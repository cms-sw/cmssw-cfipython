import FWCore.ParameterSet.Config as cms

def HGCalNeighbourCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalNeighbourCheck',
    nameDetector = cms.string('HGCalHESiliconSensitive'),
    fileName = cms.string('D120E.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
