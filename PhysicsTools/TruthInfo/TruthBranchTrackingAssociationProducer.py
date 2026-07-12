import FWCore.ParameterSet.Config as cms

def TruthBranchTrackingAssociationProducer(*args, **kwargs):
  mod = cms.EDProducer('TruthBranchTrackingAssociationProducer',
    src = cms.InputTag('truthLogicalGraphProducer'),
    hitIndex = cms.InputTag('truthLogicalGraphHitIndexProducer'),
    tracks = cms.InputTag('generalTracks'),
    interestingPdgIds = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
