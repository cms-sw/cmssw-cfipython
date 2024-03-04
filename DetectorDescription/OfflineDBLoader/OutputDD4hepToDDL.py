import FWCore.ParameterSet.Config as cms

def OutputDD4hepToDDL(**kwargs):
  mod = cms.EDAnalyzer('OutputDD4hepToDDL',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
