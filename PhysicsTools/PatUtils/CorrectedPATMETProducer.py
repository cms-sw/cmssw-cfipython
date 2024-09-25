import FWCore.ParameterSet.Config as cms

def CorrectedPATMETProducer(*args, **kwargs):
  mod = cms.EDProducer('CorrectedPATMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
