import FWCore.ParameterSet.Config as cms

def OutputDDToDDL(**kwargs):
  mod = cms.EDAnalyzer('OutputDDToDDL',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
