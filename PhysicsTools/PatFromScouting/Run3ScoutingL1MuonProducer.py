import FWCore.ParameterSet.Config as cms

def Run3ScoutingL1MuonProducer(*args, **kwargs):
  mod = cms.EDProducer('Run3ScoutingL1MuonProducer',
    muonSource = cms.InputTag('gtStage2Digis', 'Muon'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
