import FWCore.ParameterSet.Config as cms

from .EDMtoMEConverter import EDMtoMEConverter

EDMtoMEConverter = EDMtoMEConverter(

  Name = 'EDMtoMEConverter',
  lumiInputTag = ('MEtoEDMConverter', 'MEtoEDMConverterLumi'),
  reScope = 'JOB',
  runInputTag = ('MEtoEDMConverter', 'MEtoEDMConverterRun')
)
