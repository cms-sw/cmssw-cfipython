import FWCore.ParameterSet.Config as cms

def ExtraFromSeeds(*args, **kwargs):
  mod = cms.EDProducer('ExtraFromSeeds',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
