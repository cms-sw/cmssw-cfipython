import FWCore.ParameterSet.Config as cms

def ProduceAgingObject(*args, **kwargs):
  mod = cms.EDAnalyzer('ProduceAgingObject',
    dtRegEx = cms.vstring(),
    rpcRegEx = cms.vstring(),
    cscRegEx = cms.vstring(),
    maskedGEMIDs = cms.vint32(),
    maskedME0IDs = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
