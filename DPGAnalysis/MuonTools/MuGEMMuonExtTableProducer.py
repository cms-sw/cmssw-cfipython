import FWCore.ParameterSet.Config as cms

def MuGEMMuonExtTableProducer(*args, **kwargs):
  mod = cms.EDProducer('MuGEMMuonExtTableProducer',
    name = cms.string('muon'),
    src = cms.InputTag('patMuons'),
    fillPropagated = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
