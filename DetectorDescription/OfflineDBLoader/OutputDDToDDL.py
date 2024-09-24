import FWCore.ParameterSet.Config as cms

def OutputDDToDDL(*args, **kwargs):
  mod = cms.EDAnalyzer('OutputDDToDDL',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
