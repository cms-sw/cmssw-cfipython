import FWCore.ParameterSet.Config as cms

def CorrMETDataExtractor(**kwargs):
  mod = cms.EDProducer('CorrMETDataExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
