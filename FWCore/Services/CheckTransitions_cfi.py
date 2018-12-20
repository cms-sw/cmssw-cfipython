import FWCore.ParameterSet.Config as cms

CheckTransitions = cms.Service('CheckTransitions',
  transitions = cms.untracked.VPSet(
    cms.PSet()
  )
)
