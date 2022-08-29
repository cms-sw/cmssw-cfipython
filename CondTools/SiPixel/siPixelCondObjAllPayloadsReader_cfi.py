import FWCore.ParameterSet.Config as cms

siPixelCondObjAllPayloadsReader = cms.EDAnalyzer('SiPixelCondObjAllPayloadsReader',
  payloadType = cms.string('HLT'),
  mightGet = cms.optional.untracked.vstring
)
