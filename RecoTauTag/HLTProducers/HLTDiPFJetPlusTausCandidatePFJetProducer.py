import FWCore.ParameterSet.Config as cms

def HLTDiPFJetPlusTausCandidatePFJetProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTDiPFJetPlusTausCandidatePFJetProducer',
    pfJetSrc = cms.InputTag('hltAK4PFJetsCorrected'),
    tauSrc = cms.InputTag('hltSinglePFTau20TrackPt1LooseChargedIsolationReg'),
    extraTauPtCut = cms.double(45),
    mjjMin = cms.double(500),
    dRmin = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
