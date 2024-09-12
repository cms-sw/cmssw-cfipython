import FWCore.ParameterSet.Config as cms

def L1GTFinOrBoardWriter(**kwargs):
  mod = cms.EDAnalyzer('L1GTFinOrBoardWriter',
    filename = cms.required.untracked.string,
    fileExtension = cms.untracked.string('txt'),
    algoBlocksTag = cms.required.untracked.InputTag,
    channelsLow = cms.required.untracked.vuint32,
    channelsMid = cms.required.untracked.vuint32,
    channelsHigh = cms.required.untracked.vuint32,
    channelFinOr = cms.required.untracked.uint32,
    maxFrames = cms.untracked.uint32(1024),
    maxEvents = cms.untracked.uint32(0),
    patternFormat = cms.untracked.string('EMPv2'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
