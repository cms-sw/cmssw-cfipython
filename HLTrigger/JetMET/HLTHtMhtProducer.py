import FWCore.ParameterSet.Config as cms

def HLTHtMhtProducer(**kwargs):
  mod = cms.EDProducer('HLTHtMhtProducer',
    usePt = cms.bool(False),
    excludePFMuons = cms.bool(False),
    minNJetHt = cms.int32(0),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(40),
    minPtJetMht = cms.double(30),
    maxEtaJetHt = cms.double(3),
    maxEtaJetMht = cms.double(5),
    jetsLabel = cms.InputTag('hltCaloJetL1FastJetCorrected'),
    pfCandidatesLabel = cms.InputTag('hltParticleFlow'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
