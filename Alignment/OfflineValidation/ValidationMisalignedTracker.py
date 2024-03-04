import FWCore.ParameterSet.Config as cms

def ValidationMisalignedTracker(**kwargs):
  mod = cms.EDAnalyzer('ValidationMisalignedTracker',
    label = cms.VInputTag(),
    label_tp_effic = cms.InputTag('FinalTrackRefitter'),
    label_tp_fake = cms.InputTag('TrackRefitter'),
    associators = cms.vstring(),
    selection_eff = cms.untracked.bool(False),
    selection_fake = cms.untracked.bool(True),
    ZmassSelection = cms.untracked.bool(False),
    simobject = cms.untracked.string('g4SimHits'),
    TrackAssociator = cms.untracked.string('ByHits'),
    rootfile = cms.untracked.string('myroot.root'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
