import FWCore.ParameterSet.Config as cms

def ShiftedPATTauProducer(*args, **kwargs):
  mod = cms.EDProducer('ShiftedPATTauProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
