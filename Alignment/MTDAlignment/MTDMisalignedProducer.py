import FWCore.ParameterSet.Config as cms

def MTDMisalignedProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('MTDMisalignedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
