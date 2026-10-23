import FWCore.ParameterSet.Config as cms

def EcalSrFlagColMerger(*args, **kwargs):
  mod = cms.EDProducer('EcalSrFlagColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
