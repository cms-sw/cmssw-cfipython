import FWCore.ParameterSet.Config as cms

def TkAlCaOverlapTagger(*args, **kwargs):
  mod = cms.EDProducer('TkAlCaOverlapTagger',
    src = cms.InputTag('generalTracks'),
    Clustersrc = cms.InputTag('ALCARECOTkAlCosmicsCTF0T'),
    rejectBadMods = cms.bool(False),
    BadMods = cms.vuint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
