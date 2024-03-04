import FWCore.ParameterSet.Config as cms

def HLTDQMMuonSelector(**kwargs):
  mod = cms.EDProducer('HLTDQMMuonSelector',
    objs = cms.InputTag('muons'),
    vertices = cms.InputTag('offlinePrimaryVertices'),
    selection = cms.string('et > 5'),
    muonSelectionType = cms.string('tight'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
