import FWCore.ParameterSet.Config as cms

def NuclearTrackCorrector(*args, **kwargs):
  mod = cms.EDProducer('NuclearTrackCorrector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
