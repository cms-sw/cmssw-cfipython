import FWCore.ParameterSet.Config as cms

def HcalForwardLibWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalForwardLibWriter',
    FileName = cms.FileInPath('SimG4CMS/ShowerLibraryProducer/data/fileList.txt'),
    Nbins = cms.int32(16),
    Nshowers = cms.int32(10000),
    BufSize = cms.int32(1),
    SplitLevel = cms.int32(2),
    CompressionAlgo = cms.int32(4),
    CompressionLevel = cms.int32(4),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
