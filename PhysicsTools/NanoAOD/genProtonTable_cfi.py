import FWCore.ParameterSet.Config as cms

genProtonTable = cms.EDProducer('GenProtonTableProducer',
  srcPruned = cms.InputTag('prunedGenParticles'),
  srcPUProtons = cms.InputTag('genPUProtons'),
  srcAltPUProtons = cms.InputTag('genPUProtons', 'genPUProtons'),
  cut = cms.string(''),
  name = cms.string('GenProton'),
  doc = cms.string('generator level information on (signal+PU) protons'),
  tolerance = cms.double(0.001),
  mightGet = cms.optional.untracked.vstring
)
