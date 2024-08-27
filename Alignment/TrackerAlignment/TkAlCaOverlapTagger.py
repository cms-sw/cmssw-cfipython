import FWCore.ParameterSet.Config as cms

def TkAlCaOverlapTagger(**kwargs):
  mod = cms.EDProducer('TkAlCaOverlapTagger',
    src = cms.InputTag('generalTracks'),
    Clustersrc = cms.InputTag('ALCARECOTkAlCosmicsCTF0T'),
    rejectBadMods = cms.bool(False),
    BadMods = cms.vuint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
