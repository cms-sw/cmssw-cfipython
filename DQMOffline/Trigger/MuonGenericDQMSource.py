import FWCore.ParameterSet.Config as cms

def MuonGenericDQMSource(*args, **kwargs):
  mod = cms.EDProducer('MuonGenericDQMSource',
    src = cms.required.InputTag,
    folder = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
