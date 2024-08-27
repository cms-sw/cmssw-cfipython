import FWCore.ParameterSet.Config as cms

def MuGEMMuonExtTableProducer(**kwargs):
  mod = cms.EDProducer('MuGEMMuonExtTableProducer',
    name = cms.string('muon'),
    src = cms.InputTag('patMuons'),
    fillPropagated = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
