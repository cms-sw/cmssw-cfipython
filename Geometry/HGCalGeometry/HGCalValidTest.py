import FWCore.ParameterSet.Config as cms

def HGCalValidTest(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalValidTest',
    detector = cms.string('HGCalHEScintillatorSensitive'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
