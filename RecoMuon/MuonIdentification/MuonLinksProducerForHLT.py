import FWCore.ParameterSet.Config as cms

def MuonLinksProducerForHLT(*args, **kwargs):
  mod = cms.EDProducer('MuonLinksProducerForHLT',
    LinkCollection = cms.InputTag('hltPFMuonMerging'),
    InclusiveTrackerTrackCollection = cms.InputTag('hltL3MuonsLinksCombination'),
    ptMin = cms.double(2.5),
    pMin = cms.double(2.5),
    shareHitFraction = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
