import FWCore.ParameterSet.Config as cms

def NuclearTrackCorrector(**kwargs):
  mod = cms.EDProducer('NuclearTrackCorrector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
