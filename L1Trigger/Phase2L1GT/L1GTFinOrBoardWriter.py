import FWCore.ParameterSet.Config as cms

def L1GTFinOrBoardWriter(**kwargs):
  mod = cms.EDAnalyzer('L1GTFinOrBoardWriter',
    outputFilename = cms.required.string,
    outputFileExtension = cms.string('txt'),
    algoBlocksTag = cms.required.InputTag,
    channelsLow = cms.required.vuint32,
    channelsMid = cms.required.vuint32,
    channelsHigh = cms.required.vuint32,
    channelFinOr = cms.required.uint32,
    maxLines = cms.uint32(1024),
    patternFormat = cms.string('EMPv2'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
