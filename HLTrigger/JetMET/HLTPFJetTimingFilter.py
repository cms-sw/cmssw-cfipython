import FWCore.ParameterSet.Config as cms

def HLTPFJetTimingFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTPFJetTimingFilter',
    saveTags = cms.bool(True),
    jets = cms.InputTag('hltDisplacedHLTCaloJetCollectionProducerMidPt'),
    jetTimes = cms.InputTag('hltDisplacedHLTCaloJetCollectionProducerMidPtTiming'),
    jetCellsForTiming = cms.InputTag('hltDisplacedHLTCaloJetCollectionProducerMidPtTiming', 'jetCellsForTiming'),
    jetEcalEtForTiming = cms.InputTag('hltDisplacedHLTCaloJetCollectionProducerMidPtTiming', 'jetEcalEtForTiming'),
    minJets = cms.uint32(1),
    jetTimeThresh = cms.double(1),
    jetMaxTimeThresh = cms.double(999999),
    jetCellsForTimingThresh = cms.uint32(5),
    jetEcalEtForTimingThresh = cms.double(10),
    minJetPt = cms.double(40),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
