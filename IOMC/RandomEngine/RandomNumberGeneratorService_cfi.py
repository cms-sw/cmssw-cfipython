import FWCore.ParameterSet.Config as cms

RandomNumberGeneratorService = cms.Service('RandomNumberGeneratorService',
  restoreStateTag = cms.untracked.InputTag(''),
  saveFileName = cms.untracked.string(''),
  restoreFileName = cms.untracked.string(''),
  enableChecking = cms.untracked.bool(False),
  eventSeedOffset = cms.untracked.uint32(0),
  verbose = cms.untracked.bool(False),
  allowAnyLabel_ = cms.required.PSetTemplate(
    initialSeed = cms.optional.untracked.uint32,
    initialSeedSet = cms.optional.untracked.vuint32,
    engineName = cms.optional.untracked.string
  )
)
