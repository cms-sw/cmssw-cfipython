import FWCore.ParameterSet.Config as cms

def HGCalValidTest(**kwargs):
  mod = cms.EDAnalyzer('HGCalValidTest',
    detector = cms.string('HGCalHEScintillatorSensitive'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
