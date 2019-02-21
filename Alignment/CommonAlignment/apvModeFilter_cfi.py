import FWCore.ParameterSet.Config as cms

apvModeFilter = cms.EDFilter('APVModeFilter',
  apvMode = cms.untracked.string('deco')
)
