import FWCore.ParameterSet.Config as cms

def SwitchProducerProvenanceAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SwitchProducerProvenanceAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
