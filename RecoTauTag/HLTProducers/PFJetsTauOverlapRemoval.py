import FWCore.ParameterSet.Config as cms

def PFJetsTauOverlapRemoval(*args, **kwargs):
  mod = cms.EDProducer('PFJetsTauOverlapRemoval',
    PFJetSrc = cms.InputTag('hltAK4PFJetsCorrected'),
    TauSrc = cms.InputTag('hltSinglePFTau20TrackPt1LooseChargedIsolationReg'),
    Min_dR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
