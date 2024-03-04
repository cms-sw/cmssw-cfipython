import FWCore.ParameterSet.Config as cms

def L1GTBoardWriter(**kwargs):
  mod = cms.EDAnalyzer('L1GTBoardWriter',
    outputFilename = cms.required.string,
    outputFileExtension = cms.string('txt'),
    algoBlocksTag = cms.required.InputTag,
    channels = cms.required.vuint32,
    algoBitMask = cms.vuint64(),
    maxLines = cms.uint32(1024),
    patternFormat = cms.string('EMPv2'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
