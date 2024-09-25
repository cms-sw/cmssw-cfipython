import FWCore.ParameterSet.Config as cms

def HLTBTagHarvestingAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('HLTBTagHarvestingAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
