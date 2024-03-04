import FWCore.ParameterSet.Config as cms

def PFTauL1TJetsMatching(**kwargs):
  mod = cms.EDProducer('PFTauL1TJetsMatching',
    L1JetSrc = cms.InputTag('hltL1VBFDiJetOR'),
    TauSrc = cms.InputTag('hltSelectedPFTausTrackFindingLooseChargedIsolationAgainstMuon'),
    MatchingdR = cms.double(0.5),
    MinTauPt = cms.double(20),
    MinL1TPt = cms.double(115),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
