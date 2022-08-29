import FWCore.ParameterSet.Config as cms

GTTFileReader = cms.EDProducer('GTTFileReader',
  files = cms.vstring('gttOutput_0.txt'),
  format = cms.untracked.string('APx'),
  mightGet = cms.optional.untracked.vstring
)
