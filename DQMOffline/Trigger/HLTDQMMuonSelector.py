import FWCore.ParameterSet.Config as cms

def HLTDQMMuonSelector(*args, **kwargs):
  mod = cms.EDProducer('HLTDQMMuonSelector',
    objs = cms.InputTag('muons'),
    vertices = cms.InputTag('offlinePrimaryVertices'),
    selection = cms.string('et > 5'),
    muonSelectionType = cms.string('tight'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
