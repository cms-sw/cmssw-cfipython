import FWCore.ParameterSet.Config as cms

def HLTMhtProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTMhtProducer',
    usePt = cms.bool(True),
    excludePFMuons = cms.bool(False),
    minNJet = cms.int32(0),
    minPtJet = cms.double(0),
    maxEtaJet = cms.double(999),
    jetsLabel = cms.InputTag('hltAntiKT4PFJets'),
    pfCandidatesLabel = cms.InputTag('hltParticleFlow'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
