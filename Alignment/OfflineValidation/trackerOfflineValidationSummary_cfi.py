import FWCore.ParameterSet.Config as cms

trackerOfflineValidationSummary = cms.EDAnalyzer('TrackerOfflineValidationSummary',
  moduleDirectoryInOutput = cms.string('Alignment/Tracker'),
  useFit = cms.bool(False),
  stripYDmrs = cms.bool(False),
  minEntriesPerModuleForDmr = cms.uint32(100),
  TH1DmrXprimeStripModules = cms.PSet(
    Nbinx = cms.int32(100),
    xmin = cms.double(-5),
    xmax = cms.double(5)
  ),
  TH1DmrYprimeStripModules = cms.PSet(
    Nbinx = cms.int32(100),
    xmin = cms.double(-5),
    xmax = cms.double(5)
  ),
  TH1DmrXprimePixelModules = cms.PSet(
    Nbinx = cms.int32(100),
    xmin = cms.double(-5),
    xmax = cms.double(5)
  ),
  TH1DmrYprimePixelModules = cms.PSet(
    Nbinx = cms.int32(100),
    xmin = cms.double(-5),
    xmax = cms.double(5)
  ),
  mightGet = cms.optional.untracked.vstring
)
