import FWCore.ParameterSet.Config as cms

LoadAllDictionaries = cms.Service('LoadAllDictionaries',
  doLoad = cms.untracked.bool(True)
)
