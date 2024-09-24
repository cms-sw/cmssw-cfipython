import FWCore.ParameterSet.Config as cms

def OutputDD4hepToDDL(*args, **kwargs):
  mod = cms.EDAnalyzer('OutputDD4hepToDDL',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
